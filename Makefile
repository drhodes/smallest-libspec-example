PY=uv run python
SPEC_BUILD=spec-build
LIBSPEC=uv run libspec


.PHONY: spec
spec: $(SPECS)
	$(LIBSPEC) build ./spec/main_spec.py

.PHONY: diff
diff:
	$(LIBSPEC) diff $(SPEC_BUILD) 

.PHONY: test-mcp
test-mcp: 
	npx @modelcontextprotocol/inspector uv run libspec-mcp
