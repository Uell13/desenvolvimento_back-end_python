import os
import time
import secrets
import shlex
import json
from datetime import datetime
from rich import print
from rich.table import Table


class GerenciadorDeTarefas:
    def __init__(self):
        self._arquivo = 'tarefas.json'
        self._tarefas = self._carregar_dados()

    def _limpar_terminal(self):
        return os.system('cls' if os.name == 'nt' else 'clear')

    def _enter_continue(self):
        return input('Pressione Enter para continuar... ')

    def _exibe_menu_opcoes(self) -> str:
        return ('--- [blue]MENU - GERENCIADOR DE TAREFAS[/] ---\n\n'
                '1. Adicionar tarefa\n'
                '2. Visualizar tarefas\n'
                '3. Sair')

    def _carregar_dados(self):
        """Lê o arquivo JSON. Se não existir, retorna uma string vazia."""
        if not os.path.exists(self._arquivo):
            return {}
        try:
            with open(self._arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def _salvar_dados(self):
        with open(self._arquivo, 'w', encoding='utf-8') as f:
            json.dump(self._tarefas, f, indent=4, ensure_ascii=False)

    def _adicionar_tarefa(self, tarefa: str) -> bool:
        id_curto = secrets.token_urlsafe(4)
        while id_curto in self._tarefas:
            id_curto = secrets.token_urlsafe(4)
        self._tarefas[id_curto] = {
            'tarefa': tarefa,
            'criado_em': datetime.now().strftime('%d/%m/%Y - %H:%M'),
            'status': False
        }
        self._salvar_dados()
        return True

    def _visualizar_tarefas(self) -> Table:
        tabela = Table(title='Minhas tarefas')
        tabela.add_column('ID')
        tabela.add_column('Tarefa')
        tabela.add_column('Criado em')
        tabela.add_column('Status')
        for id_tarefa, info in self._tarefas.items():
            status = '[green bold]Concluído[/]' if info['status'] else '[red bold]Pendente[/]'
            tabela.add_row(
                id_tarefa,
                info['tarefa'],
                info['criado_em'],
                status
            )
        return tabela

    def _remover_tarefa(self, id: str) -> bool:
        if id not in self._tarefas:
            return False
        self._tarefas.pop(id)
        self._salvar_dados()
        return True

    def _alterar_status(self, id: str) -> bool:
        if id not in self._tarefas:
            return False
        self._tarefas[id]['status'] = not self._tarefas[id]['status']
        self._salvar_dados()
        return True

    def _fluxo_visualizacao(self):
        while True:
            self._limpar_terminal()

            if not self._tarefas:
                print('[yellow]Nenhuma tarefa encontrada![/]')
                self._enter_continue()
                break

            resultado = self._visualizar_tarefas()
            print('[yellow]LISTA DE COMANDOS[/]\n'
                  '[purple bold]/menu[/] -- Volta ao menu principal\n'
                  '[purple bold]/criar_tarefa "nova tarefa"[/] -- Cria uma nova tarefa\n'
                  '[purple bold]/apagar_tarefa <id da tarefa>[/] -- Apagar a tarefa informada pelo ID\n'
                  '[purple bold]/alterar_status <id da tarefa>[/] -- Altera o status da tarefa informada pelo ID\n'
            )
            print(resultado)

            resposta = shlex.split(input('comando: '))
            if not resposta:
                continue

            cmd = resposta[0]
            if cmd == '/menu':
                break
            elif cmd == '/criar_tarefa' and len(resposta) == 2:
                if self._adicionar_tarefa(resposta[1]):
                    print(
                        f'\n[green]Sucesso:[/] Tarefa adionada.')
                self._enter_continue()
            elif cmd == '/apagar_tarefa' and len(resposta) == 2:
                if self._remover_tarefa(resposta[1]):
                    print(
                        f'\n[green]Sucesso:[/] Tarefa {resposta[1]} apagada.')
                else:
                    print('\n[red]Erro:[/] ID não encontrado.')
                self._enter_continue()
            elif cmd == '/alterar_status' and len(resposta) == 2:
                if self._alterar_status(resposta[1]):
                    print(
                        f'\n[green]Sucesso:[/] Status de {resposta[1]} alterado.')
                else:
                    print('\n[red]Erro:[/] ID não encontrado.')
                self._enter_continue()
            else:
                print('\n[red]Comando inválido ou ID faltando![/]')
                time.sleep(1)

    def main(self):
        while True:
            self._limpar_terminal()
            print(self._exibe_menu_opcoes())

            try:
                opcao = int(input('\nEscolha uma opção: '))
            except ValueError:
                print('[red]Por favor, digite apenas números.[/]')
                time.sleep(1)
                continue

            if opcao == 1:
                tarefa = input('Tarefa: ')
                if tarefa.strip():
                    self._adicionar_tarefa(tarefa)
                    print('[green]Tarefa salva![/]')
                time.sleep(1)
            elif opcao == 2:
                self._fluxo_visualizacao()
            elif opcao == 3:
                print('Saindo do gerenciador de tarefas. Até mais!')
                break
            else:
                print('[red]Opção inválida![/]')
                time.sleep(1)


if __name__ == '__main__':
    g1 = GerenciadorDeTarefas()
    g1.main()
