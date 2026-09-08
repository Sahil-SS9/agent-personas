# Security

Treat downloaded instructions and executable scripts as code you must review. Skills cannot grant permissions or override your host policy.

The trial helper writes into a new destination and does not modify live profiles. The execution helper passes literal arguments without a shell, uses an environment allowlist and bounds time and output. It is not a security sandbox: your agent CLI may still use its normal account and filesystem access. Use the CLI’s own permission and isolation controls.

Do not put credentials in prompts, argument arrays or reports. Basic output redaction is not comprehensive privacy filtering. Inspect any transcript before sharing.

The catalogue manifest checks integrity and completeness but is not a cryptographic signature; an attacker controlling both content and manifest can replace them. Obtain releases from a trusted publisher and pin the reviewed revision.

Report non-sensitive defects through repository issues. Do not post exploit secrets or customer data publicly. Contact the repository owner privately for sensitive disclosures; no dedicated security response SLA is promised.
