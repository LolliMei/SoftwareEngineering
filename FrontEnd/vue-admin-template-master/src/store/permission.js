import {asyncRouterMap, constantRouterMap} from '../router/index';
import Vue from 'vue'


const permission = {
    actions: {

      GenerateRoutes(roles) {
        // 根据权限 筛选路由
        function filterAsyncRouter(asyncRouterMap, roles) {
          const accessedRouters = asyncRouterMap.filter(route => {
            if (route.meta.roles.indexOf(roles) >= 0) {
              if (route.children && route.children.length) {
                route.children = filterAsyncRouter(route.children, roles)
              }
              return true
            }
            return false
          });
          return accessedRouters
        }

        return filterAsyncRouter(asyncRouterMap, roles)
      },

    }
  }
;

export default permission;
