import ast

ALLOWED_NODES = (
    ast.Expression, ast.BoolOp, ast.BinOp, ast.UnaryOp,
    ast.Compare, ast.Name, ast.Load, ast.Constant,
    ast.And, ast.Or, ast.Not,
    ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE,
    ast.Mod
)

ALLOWED_NAMES = {"h", "m", "s"}

def safe_eval(expr: str, context: dict) -> bool:
    tree = ast.parse(expr, mode="eval")

    for node in ast.walk(tree):
        if not isinstance(node, ALLOWED_NODES):
            raise ValueError("Expression non autorisée")
        if isinstance(node, ast.Name) and node.id not in ALLOWED_NAMES:
            raise ValueError(f"Nom interdit : {node.id}")

    return bool(eval(compile(tree, "<expr>", "eval"), {}, context))
