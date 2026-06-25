<template>
  <nav>

    <router-link to="/">
      🏠 Início
    </router-link>

    |

    <router-link to="/cadastros">
      📝 Cadastros
    </router-link>

    |

    <router-link to="/consultas">
      🔎 Consultas
    </router-link>

    |

    <router-link to="/notas">
      📊 Notas
    </router-link>

  </nav>
</template>

<style scoped>
nav{
  padding:20px;
}

a{
  margin:10px;
  text-decoration:none;
}
</style>