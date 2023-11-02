import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import NewMascotas from '@/components/Mascotas/NewMascotas'
import ListMascotas from '@/components/Mascotas/ListMascotas'
import EditMascotas from '@/components/Mascotas/EditMascotas'
import DeleteMascotas from '@/components/Mascotas/DeleteMascotas'
import DetailPersona from '@/components/Mascotas/DetailPersona'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/mascotas',
      name: 'ListMascotas',
      component: ListMascotas
    },
    {
      path: '/mascotas/new',
      name: 'NewMascotas',
      component: NewMascotas
    },
    {
      path: '/mascotas/:mascotaId/edit',
      name: 'EditMascotas',
      component: EditMascotas
    },
    {
      path: '/mascotas/:mascotaId/delete',
      name: 'DeleteMascotas',
      component: DeleteMascotas
    },
    {
      path: '/mascotas/:personaId/persona',
      name: 'DetailPersona',
      component: DetailPersona
    }
  ],
  mode: 'history'
})
