import { createI18n } from "vue-i18n";
import ruRU from './ru-RU.json';
import enEN from './en-EN.json';


let locale = localStorage.getItem('locale');

if (locale == null) {
    locale = 'ru-RU'
    localStorage.setItem('locale',locale);
}

const i18n = createI18n({
    locale: locale,
    fallbackLocale: 'ru-RU',
    messages: {
        'ru-RU':ruRU,
        'en-EN':enEN
    }
})

export default i18n;