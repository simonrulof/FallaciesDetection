import os
from pyswip import Prolog
from swiplserver import PrologMQI, PrologThread, create_posix_path


class PrologManager:

    def launchProlog(reasoning, goal):
        """
        use the reasoning and goal variables to check if there is a fallacy or not.
        @param reasoning: reasonning which supposely lead to the conclusion
        @param goal: the conclusion.
        @return: results of the prolog file.
        """
        #cloning a new file to use (in case of crash to not lose the file in case of crash.
        os.system("cp ./Prolog/kb_classical_logic.pl ./Prolog/.temp.pl")
        file = open('./Prolog/.temp.pl', 'a')

        # adding the argument and the facts to the file.
        argument = 'argument(arg, ['
        for reason in reasoning:
            file.write("fact(" + reason + ").\n")
            argument = argument + reason + ','

        argument = argument[:-1] + '], ' + goal + ').'
        file.write(argument)
        file.close()

        #using swiplserver, checkin if these facts and the arguments lead to the desired goal and with which scheme.
        with PrologMQI() as mqi:
            with mqi.create_thread() as prolog:
                path = create_posix_path("./Prolog/.temp.pl")
                prolog.query(f'consult("{path}").')
                result = prolog.query('prove(' + goal + ', X).')
                os.system('rm ./Prolog/.temp.pl')
                return result
