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

# Query que regresa canciones filtradas por genero
query{
  cancionesPorGenero(genero:"genero"){
    nombre
    duracion
    album {
      id
      
    }
  }
}

# Query que regresa canciones filtradas por subgenero
query{
  cancionesPorGenero(subgenero:"subgenero"){
    nombre
    duracion
    album {
      id
      
    }
  }
}
