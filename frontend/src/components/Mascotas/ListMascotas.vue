<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Listado de Mascotas</h2>
        <b-button size="sm" :to="{name: 'NewMascotas'}" variant="primary">Nuevo Libro</b-button>
        <div class="col-md-15">
          <b-table striped hover :items="mascotas" :fields="fields">
            <template v-slot:cell(acciones)="data">
              <b-button size="sm" variant="info" :to="{name: 'DetailPersona', params: {mascotaId: data.item.id}}">
                Ver Adoptante
              </b-button>
              <b-button size="sm" variant="primary" :to="{name: 'EditMascotas', params: {mascotaId: data.item.id}}">
                Editar
              </b-button>
              <b-button size="sm" variant="danger" :to="{name: 'DeleteMascotas', params: {mascotaId: data.item.id}}">
                Eliminar
              </b-button>
            </template>
          </b-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      fields: [
        { key: 'id', label: '#'},
        { key: 'nombre', label: 'Nombre'},
        { key: 'sexo', label: 'Sexo'},
        { key: 'edad_aproximada', label: 'Edad'},
        { key: 'fecha_rescate', label: 'Fecha de Rescate'},
        { key: 'vacuna', label: 'Vacunas',
          formatter: (value) => {
            return Array.isArray(value) ? value.map(v => v.nombre).join(', ') : '';
          }
        },
        { key: 'persona.nombre',
          label: 'Adoptante',
          formatter: (value, key, item) => {
          return `${value} ${item.persona.apellidos}`;
          }},
        { key: 'acciones', label: 'Acciones'}
      ],
      mascotas: []
    }
  },
  methods: {
    getMascotas() {
      const base_env = process.env.BASE_URI
      const base_hard = 'http://mascotasjose.net:8002/api/v2/'
      const path = base_env ? `${base_env}mascotas/` : `${base_hard}mascotas/`;
      console.log(path)
      axios.get(path).then((response) => {
        this.mascotas = response.data
        console.log(this.mascotas)
      }).catch((error) => {
        console.log("xdddddddddddd")
        console.log(error)
      })
    }
  },
  created() {
    this.getMascotas()
  }
}
</script>

<style lang="css" scoped>
</style>
