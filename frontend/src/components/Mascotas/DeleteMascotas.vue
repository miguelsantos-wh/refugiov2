<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col">
        <h3>¿Estas seguro que deseas eliminar esta mascota?</h3>
        <p>Mascota: {{ this.element.nombre }}</p>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <b-button v-on:click="deleteMascota" variant="danger">Eliminar</b-button>
        <b-button type="submit" class="btn-large-space" :to="{name: 'ListMascotas'}">Cancelar</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import swal from "sweetalert";
export default {
  data() {
    return {
      mascotaId: this.$route.params.mascotaId,
      element: {
        nombre: ''
      }
    }
  },
  methods: {
    getMascota() {
      const base_env = process.env.BASE_URI
      const base_hard = 'http://mascotasjose.net:8002/api/v2/'
      const path = base_env ? `${base_env}mascotas/${this.mascotaId}/` : `${base_hard}mascotas/${this.mascotaId}/`;
      axios.get(path).then((response) => {
        this.element.nombre = response.data.nombre
        console.log(response.data)
      }).catch((error) => {
        console.log(error)
      })
    },

    deleteMascota() {
      const base_env = process.env.BASE_URI
      const base_hard = 'http://mascotasjose.net:8002/api/v2/'
      const path = base_env ? `${base_env}mascotas/${this.mascotaId}/` : `${base_hard}mascotas/${this.mascotaId}/`;
      axios.delete(path).then((response) => {
        location.href = "/mascotas"
        console.log(response.data)
      }).catch((error) => {
        swal("No es posible eliminar el libro ${error}", "", "error")
      })
    }
  },
  created() {
    this.getMascota()
  }
}
</script>

<style scoped>

</style>
