<template>
  <nav class="navbar">

    <router-link to="/">
      Início
    </router-link>

    <router-link to="/cadastros">
      Cadastros
    </router-link>
<router-link to="/relatorios">
      Relatórios
    </router-link>
    

  </nav>
</template>

<style scoped>

.navbar{
  background:#1e293b;
  padding:15px;

  display:flex;
  justify-content:center;
  gap:20px;
}

a{
  color:white;
  text-decoration:none;
  font-weight:bold;
}

.router-link-active{
  color:#38bdf8;
}

</style>