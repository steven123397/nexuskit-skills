"""Parse skill metadata safely without imposing a client-specific field allowlist."""
import yaml
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML with duplicate mapping keys treated as errors at every depth."""

    def construct_mapping(self, node, deep=False):
        if not isinstance(node, MappingNode):
            return super().construct_mapping(node, deep=deep)
        self.flatten_mapping(node)
        seen = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                if key in seen:
                    raise ConstructorError(
                        "while constructing a mapping", node.start_mark,
                        f"duplicate key {key!r}", key_node.start_mark,
                    )
                seen.add(key)
            except TypeError as exc:
                raise ConstructorError(
                    "while constructing a mapping", node.start_mark,
                    "unhashable mapping key", key_node.start_mark,
                ) from exc
        return super().construct_mapping(node, deep=deep)


def validate_frontmatter(text, dirname):
    lines = text.splitlines()
    if not lines or lines[0].rstrip() != "---":
        return ["missing frontmatter"]
    end = next((i for i in range(1, len(lines)) if lines[i].rstrip() == "---"), None)
    if end is None:
        return ["unterminated frontmatter"]
    try:
        metadata = yaml.load("\n".join(lines[1:end]), Loader=UniqueKeyLoader)
    except yaml.YAMLError as exc:
        return [f"invalid YAML frontmatter: {exc}"]
    if not isinstance(metadata, dict):
        return ["frontmatter must be a mapping"]
    problems = []
    for field in ("name", "description"):
        value = metadata.get(field)
        if not isinstance(value, str) or not value.strip():
            problems.append(f"frontmatter {field} must be a non-empty string")
    name = metadata.get("name")
    if isinstance(name, str) and name.strip() and name != dirname:
        problems.append(f"name '{name}' != directory '{dirname}' (installers derive install dir from frontmatter name)")
    return problems
