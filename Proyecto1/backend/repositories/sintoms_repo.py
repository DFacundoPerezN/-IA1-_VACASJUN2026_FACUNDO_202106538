import repositories.prolog_repo as prolog_repo

class SintomsRepo(prolog_repo.PrologRepo):
    def __init__(self, prolog_file):
        super().__init__(prolog_file)

    def get_sintomas(self):
        return self.query("sintoma(X).")