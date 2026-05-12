JAZZMIN_SETTINGS = {
    "site_title": "Task Manager Admin",
    "site_header": "Task Manager",
    "site_brand": "Task Manager",

    "welcome_sign": "Добро пожаловать в админ-панель",

    "copyright": "Das Mukumjanov",

    "search_model": [
        "auth.User",
        "tasks.Task",
    ],

    "topmenu_links": [
        {
            "name": "Главная",
            "url": "admin:index",
            "permissions": ["auth.view_user"],
        },
        {
            "name": "Сайт",
            "url": "/",
        },
    ],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "tasks.Task": "fas fa-list-check",
    },

    "show_sidebar": True,
    "navigation_expanded": True,

    "hide_apps": [],
    "hide_models": [],

    "order_with_respect_to": [
        "tasks",
        "tasks.Task",
        "auth",
        "auth.user",
    ],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "dark_mode_theme": "darkly",

    "navbar_small_text": False,
    "footer_small_text": False,

    "navbar_fixed": True,
    "footer_fixed": False,
    "sidebar_fixed": True,

    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,

    "sidebar_nav_child_indent": True,

    "brand_colour": "navbar-primary",
    "accent": "accent-primary",

    "navbar": "navbar-dark",
    "no_navbar_border": True,

    "sidebar": "sidebar-dark-primary",
    "sidebar_style": "sidebar-no-expand",

    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    }
}