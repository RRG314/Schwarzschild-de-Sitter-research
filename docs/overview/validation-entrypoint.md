# Validation Entrypoint

Run the strongest exact and regression checks:

```bash
cd /Users/stevenreid/Documents/sds-research-repo
./scripts/validate/run_sds_research_checks.sh
```

Then run the broader tool/docs checks:

```bash
./scripts/validate/run_sds_tools_suite.sh
node scripts/validate/check-doc-links.mjs
```
