/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                'neutral-color': '#FFFFFF',
                'primary-color-1': '#6c757d',
                'primary-color-2': '#dee2e6',
                'primary-color-3': '#adb5bd',
                'secondary-color-1': '#D36135',
                'secondary-color-2': '#af3800',
                'secondary-color-3': '#dda15e',
                'black-color': '#353535',
                'success-color': '#7cb518',
                'cancel-color': '#da2c38',
            },
            backgroundImage: {
                'hero-image-one': "url('https://d1kzjq66iwuksu.cloudfront.net/home_page/home1.jpeg')",
                'hero-image-two': "url('https://d1kzjq66iwuksu.cloudfront.net/home_page/home2.jpeg')",
                'hero-image-three': "url('https://d1kzjq66iwuksu.cloudfront.net/home_page/home3.jpeg')",
                'hero-image-four': "url('https://d1kzjq66iwuksu.cloudfront.net/home_page/home4.jpeg')",
            }
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
