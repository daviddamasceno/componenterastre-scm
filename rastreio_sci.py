"""Rastreador mínimo de SCI do ComponenteRastre."""


def registrar_sci(nome: str, versao: str) -> str:
    return f"SCI={nome};versao={versao}"


if __name__ == "__main__":
    print(registrar_sci("politica-mudanca", "0.1.0"))
