def main():
    while True:
        print("\n=== SISTEMA DE BOLETIM ESCOLAR ===")
        
        # 1. ENTRADA DE DADOS
        nome = input("Nome do Aluno: ")
        
        try:
            nota1 = float(input("Digite a 1.a Nota: "))
            nota2 = float(input("Digite a 2.a Nota: "))
            nota3 = float(input("Digite a 3.a Nota: "))
            frequencia = int(input("Digite a Frequencia (%): "))
        except ValueError:
            print("\nERRO: Digite apenas numeros!")
            continue # Volta para o inicio do loop

        # 2. PROCESSAMENTO (Calculo da Media)
        media = (nota1 + nota2 + nota3) / 3

        # 3. LOGICA DE DECISAO (If/Else)
        if media >= 7 and frequencia >= 75:
            situacao = "APROVADO"
        elif media >= 4 and frequencia >= 75:
            situacao = "EM RECUPERACAO"
        elif frequencia < 75:
            situacao = "REPROVADO POR FALTA"
        else:
            situacao = "REPROVADO POR NOTA"

        # 4. SAIDA DE DADOS
        print("-" * 30)
        print(f"Aluno: {nome}")
        print(f"Media Final: {media:.1f}")
        print(f"Frequencia: {frequencia}%")
        print(f"Situacao: {situacao}")
        print("-" * 30)

        # Pergunta para sair
        opcao = input("Calcular outro aluno? (S/N): ").upper()
        if opcao != 'S':
            print("Encerrando o sistema...")
            break

if __name__ == "__main__":
    main()