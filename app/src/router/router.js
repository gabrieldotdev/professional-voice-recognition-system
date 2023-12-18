// Routes.js
import { LayoutDefault, LayoutNone } from '../components/layouts';
import { Home, Login, Register } from '../pages';

export const PublicRoutes = [
    {
        path: '/',
        component: Home,
        layout: LayoutDefault,
        isPrivate: false,
    },
    {
        path: '/auth/login',
        component: Login,
        layout: LayoutNone,
        isPrivate: false,
    },
    {
        path: '/auth/new/register',
        component: Register,
        layout: LayoutNone,
        isPrivate: false,
    },
];

export const PrivateRoutes = [];
