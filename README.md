# monoku_prueba
Prueba backend monoku

# query que regresa todas las canciones 
{
  allCanciones {
    id
    nombre
    duracion
  }
}

# Mutacion que crea un artista
mutation{
  creaArtista(bandaId:2,nombre:"daft punk"){
    artista{
      id
      nombre
    }
  }
}

