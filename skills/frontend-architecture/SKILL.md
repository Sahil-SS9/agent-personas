---
name: "frontend-architecture"
description: "Structure frontend code: state ownership, data fetching, and component boundaries."
license: "MIT"
---

# Frontend Architecture

Decide where state lives and how data flows before writing components.

## 1. Own state at the right level
- Local state for local concerns; lift only when two siblings must agree.
- Server state (fetched) is not UI state: cache it, revalidate it, don't copy it into local state.
- Global store only for genuinely cross-cutting state (auth, theme); most state is not global.

## 2. Data fetching is a contract
- Fetch at the boundary that owns the data; pass down, don't re-fetch in leaves.
- Model loading, empty, error and success as explicit states, never just "no data yet".
- Colocate the query with the component that needs it; avoid waterfall fetches.

## 3. Component boundaries by responsibility
- Split by responsibility and reuse, not by line count.
- Container (data/logic) vs presentational (props in, markup out) keeps testability high.
- Props are an API: minimal, typed, no leaking internal shape.

## 4. Worked example

Input scenario: a team inbox shows a conversation list and a detail pane. Selecting a conversation loads its messages. A star toggle in the detail header updates the same conversation's row in the list. Search filters the list on the server. Assume `getConversation(id)`, `getMessages(id)` and `starConversation(id, on)` already exist.

### State owners and data flow

| State | Owner | Lifetime | Read by | Why not elsewhere |
|---|---|---|---|---|
| selected conversation id | page, in the URL | survives reload, shareable | list, detail | local state would break refresh, back button and deep links |
| conversation list | server cache, keyed by inbox and query | refetched on invalidate or focus | list | copying it into local state duplicates the truth |
| messages for the selected id | server cache, keyed by id | cached, revalidated | detail | belongs to the id that selected it |
| starred flag | server cache, optimistic write with rollback | server truth | detail header, list row | two copies drift apart on the next refetch |
| search input text | list container, local | component lifetime | list | URL only when a search must be shareable |
| split vs stacked layout | page container, local | component lifetime | layout | purely visual, nobody else needs it |

### Component sketch

```
InboxPage                     owns selection (URL) and layout (local)
├── SearchBar                 presentational: value, onChange
├── ConversationList          owns the list query; receives selectedId, onSelect
│   └── ConversationRow       presentational: props only
└── ConversationDetail        owns the messages query; receives id
    ├── DetailHeader          presentational: onToggleStar
    ├── MessageList           presentational: props only
    └── DetailStates          one branch each: loading, error, empty
```

### Checks before done
- Every fetched surface renders four named branches: loading, error with a retry, empty with the next action, success. "No data yet" is a defect, not an empty state.
- Exactly one component fetches each cache key. Count the query calls per screen; the number must match the number of distinct keys.
- No effect copies server data into local state. Search the diff for an effect that writes state derived from a query.
- Selection survives reload: refresh and the same conversation reopens, because the id lives in the URL.
- The star flips immediately and rolls back with a visible error when the write fails; the list row updates from the same source.
- Search input is debounced or carries a request id, so a stale response cannot overwrite a newer one.

### Rejected control: duplicated server state

```jsx
function Inbox({ conversationId }) {
  const [conversation, setConversation] = useState(null);
  const [messages, setMessages] = useState([]);
  useEffect(() => { getConversation(conversationId).then(setConversation); }, [conversationId]);
  useEffect(() => { getMessages(conversationId).then(setMessages); }, [conversationId]);
  const toggleStar = () => {
    setConversation({ ...conversation, starred: !conversation.starred });
    starConversation(conversationId, !conversation.starred);
  };
  if (!conversation) return null;
  return <Detail conversation={conversation} messages={messages} onToggleStar={toggleStar} />;
}
```

Reject it. Server truth is copied into two local states that the cache cannot update, so the list row and the header disagree after the next refetch. Two uncoordinated effects mean the messages request fires even when the conversation 404s, and a stale id can resolve after a newer one. There is no loading, error or empty branch, only `null`, so a failed request is indistinguishable from a slow one. The star toggle never rolls back and surfaces no error. `toggleStar` dereferences `conversation` before it exists.

## 5. Accept or reject

- Accept when every piece of state has a named owner in the table, one component fetches each cache key, and all four render states exist for each fetched surface.
- Reject when server data is copied into local state, when two components fetch the same key, or when any fetched surface renders "empty" for loading or for error.
- Reject "just add another useState" as the fix: name what should own the state instead.

## Voice
Structure-first. Refuse "just add another useState" when the real fix is moving state ownership.
