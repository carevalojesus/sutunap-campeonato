/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                'daintree': {
                    '50': '#e9ffff',
                    '100': '#c9ffff',
                    '200': '#99fcff',
                    '300': '#54f7ff',
                    '400': '#07e6ff',
                    '500': '#00c8ef',
                    '600': '#009fc9',
                    '700': '#007ea1',
                    '800': '#086582',
                    '900': '#0c536d',
                    '950': '#001923',
                },

            }
        },
    },
    plugins: [
         require('@tailwindcss/forms'),
    ],
}