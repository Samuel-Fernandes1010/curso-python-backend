class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
    
    def __repr__(self):
        return f"Música(Título={self.titulo}, Artista={self.artista}, Duração={self.duracao})"
    
    def __str__(self):
        return f"{self.titulo} - {self.artista}"

class Playlist:
    def __init__(self,nome):
        self.nome = nome
        self._musicas = []
        
    def adicionarMusica(self, musica:Musica):
        self._musicas.append(musica)
        print('Música {musica.titulo} adicionada à Playlist')
    
    def __str__(self):
        totalMusicas = len(self._musicas)
        return f"Playlist {self.nome} - {totalMusicas} músicas."
    
    def __repr__(self):
        return f"Playlist {self.nome}, {self._musicas}"
    
    def __len__(self):
        return len(self._musicas)
    
    def __getitem__(self, index):
        return self._musicas[index]
    
    def __add__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented #Indica que não é possível somar dois objetos.
        
        #Criando playlists
        novo_nome = f"Mix: {self.nome} + {other.name}"
        nova_playlist = Playlist(novo_nome)
        
        #Adicionar músicas
        for musicas in self._musicas:
            nova_playlist._musicas.append(musicas)
            
        for musicas in other:
            nova_playlist._musicas.append(musicas)
    
