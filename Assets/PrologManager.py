import os
from pyswip import Prolog
from swiplserver import PrologMQI, PrologThread, create_posix_path


class PrologManager:

    def launchProlog(reasoning, goal):
        os.system("cp ./Prolog/kb_classical_logic.pl ./Prolog/.temp.pl")
        file = open('./Prolog/.temp.pl', 'a')

        argument = 'argument(arg, ['

        for reason in reasoning:
            file.write("fact(" + reason + ").\n")
            argument = argument + reason + ','

        argument = argument[:-1] + '], ' + goal + ').'

        file.write(argument)

        file.close()


        with PrologMQI() as mqi:
            with mqi.create_thread() as prolog:
                path = create_posix_path("./Prolog/.temp.pl")
                prolog.query(f'consult("{path}").')
                result = prolog.query('prove(' + goal + ', X).')
                os.system('rm ./Prolog/.temp.pl')
                return result
