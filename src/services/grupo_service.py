from ftplib import all_errors
from tokenize import group
from ..models.grupo_model import grupo_model,grupo_bd
from ..models.times_model import times_bd
from ..repository.grupo_repository import grupo_repository
from ..repository.times_repository import times_repository


class grupo_services(object):
    _grupo_repository: grupo_repository = grupo_repository()
    _teamsRepository: times_repository = times_repository()

    def __init__(self):
        pass

    def buscar_grupo(self):
        return self._grupo_repository.get()

    def buscar_id_grupo(self, id):
        grupo = self._grupo_repository.busca_id_grupo(id);
        teams = self._teamsRepository.findTeamByGroup(grupo.id);
        grupoModel = self._bdToModel(grupo, teams)    
        return grupoModel;

    def create(self,model: grupo_model):
        grupoBd = self._modelToBd(model)
        timeBd = self._timeToBD(model)
        item = self._grupo_repository.post_grupo(grupoBd)
        model.id = item.id;

        times = self._grupo_repository.busca_id_grupo(grupoBd.id)
        times_em_grupo = self._teamsRepository.findTeamByGroup(timeBd.id_group)
        for time in times_em_grupo:
            if time == times:
                raise Exception("Existe um time associado a este grupo")
        self.updateTeam(model);

###o de cima

    def update(self, model: grupo_model):
        grupoBd = self._modelToBd(model)
        self._grupo_repository.put_grupo(grupoBd)

        teams = self._teamsRepository.findTeamByGroup(model.id);
        for team in teams:
            team.id_group = 0;
            self._teamsRepository.update(team);

        self.updateTeam(model)




    def updateTeam(self, model: grupo_model):
        allTeams = self._teamsRepository.get();
        for team in allTeams:
            for groupTeam in model.teams:
                if team.id != groupTeam:
                    continue


                team.id_group = model.id;
                self._teamsRepository.update(team)


    def delete_id_grupo(self, id: int):
        allTeams = self._teamsRepository.get();        
        
        for team in allTeams:
            if team.id_group == id:
                raise Exception("Existe um time associado a este grupo, por favor atulize-o antes de excluir");

        return self ._grupo_repository.delete_id_grupo(id)

    def _timeToBD(self,model):
        timeBd = times_bd();
        timeBd.id_group = model.id_group
        return timeBd

    def _modelToBd(self, model):
        grupoBd = grupo_bd();
        grupoBd.client_id = model.client_id;
        grupoBd.leader_id = model.leader_id;
        grupoBd.id = model.id;
        grupoBd.name = model.name;
        return grupoBd

    def _bdToModel(self, g, teams):
        grupoModel = grupo_model()
        grupoModel.id = g.id
        grupoModel.name = g.name
        grupoModel.client_id = g.client_id
        grupoModel.leader_id = g.leader_id
        grupoModel.teams = list(map(lambda x: x.id, teams))
        return grupoModel;
