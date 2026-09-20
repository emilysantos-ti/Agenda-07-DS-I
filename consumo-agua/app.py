# Sistema de Classificação de Consumo de Água
# Agenda 07 - Desenvolvimento de Sistemas

print("=" * 50)
print("💧 SISTEMA DE CLASSIFICAÇÃO DE CONSUMO DE ÁGUA 💧")
print("=" * 50)

# Solicita e valida o tipo de imóvel
tipo_imovel = input(
    "\nDigite o tipo de imóvel (comercial, casa ou apartamento): "
).strip().lower()

while tipo_imovel not in ["comercial", "casa", "apartamento"]:
    print("\n⚠️ Tipo de imóvel inválido.")
    tipo_imovel = input(
        "Digite novamente (comercial, casa ou apartamento): "
    ).strip().lower()

# Solicita e valida o consumo mensal de água
while True:
    try:
        consumo = float(
            input("\nDigite o consumo mensal de água em m³: ")
            .replace(",", ".")
        )

        if consumo < 0:
            print("\n⚠️ O consumo não pode ser negativo.")
        else:
            break

    except ValueError:
        print("\n⚠️ Digite um valor numérico válido.")

# Classificação do consumo
if tipo_imovel == "comercial":
    resultado = (
        "Tarifa COMERCIAL aplicada — consulte o plano corporativo."
    )

elif tipo_imovel == "apartamento" and consumo < 10:
    resultado = (
        "Consumo econômico — excelente controle de água!"
    )

elif tipo_imovel in ["apartamento", "casa"] and consumo <= 25:
    resultado = (
        "Consumo moderado — dentro do padrão residencial."
    )

else:
    resultado = (
        "Consumo excessivo — adote medidas de economia "
        "e verifique vazamentos."
    )

# Exibe o resultado final
print("\n" + "=" * 50)
print("📊 RESULTADO DA ANÁLISE")
print("=" * 50)
print(f"Tipo de imóvel: {tipo_imovel.capitalize()}")
print(f"Consumo mensal: {consumo:.2f} m³")
print(f"Classificação: {resultado}")
print("=" * 50)
