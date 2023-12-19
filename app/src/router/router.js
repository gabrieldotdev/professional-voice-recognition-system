// Routes.js
import { LayoutDefault } from '../components/layouts';
import { Home } from '../pages';

export const PublicRoutes = [
    {
        path: '/',
        component: Home,
        layout: LayoutDefault,
        isPrivate: false,
    },
];

export const PrivateRoutes = [];
