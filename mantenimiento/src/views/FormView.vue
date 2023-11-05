<template>
    <h1>This is the form view</h1>
    <input v-model="nombre" type="text" placeholder="Nombre completo"/><br>
    <input v-model="matricula" type="text" placeholder="A00000000"/><br>
    <input v-model="habitacion" type="text" placeholder="Num Hab."/><br>
    <input v-model="descripcion" type="text" placeholder="Describe el problema"/><br>
    <p>{{ nombre }}</p>
    <p>{{ matricula }}</p>
    <p>{{ habitacion }}</p>
    <p>{{ descripcion }}</p>
</template>

<script>
  export default {
    data() {
      return {
        nombre: "",
        matricula: "",
        habitacion: "",
        descripcion: ""
      }
    }

  }
</script>