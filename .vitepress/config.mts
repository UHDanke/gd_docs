import { defineConfig } from 'vitepress'
import sidebar from './sidebar.mts';

export default defineConfig({
  srcDir: "docs",

  title: "GD Docs",
  description: "Documentation for Geometry Dash",
  lang: 'en-US',

  sitemap: {
    hostname: 'https://boomlings.dev'
  },

  cleanUrls: true,

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: "/assets/logo.png",
    nav: [
      { text: 'Home', link: '/' }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/UHDanke/gd_docs' }
    ],

    editLink: {
      pattern: 'https://github.com/UHDanke/gd_docs/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },

    sidebar: sidebar,

    lastUpdated: true,

    search: {
      provider: 'local'
    },

    docFooter: {
      prev: false,
      next: false,
    },

    aside: false
  },

  head: [
    ["link", { rel: "icon", type: "image/png", sizes: "32x32", href: "/logo32.png" }],
    ["link", { rel: "icon", type: "image/png", sizes: "96x96", href: "/logo96.png" }],
    ["link", { rel: "icon", type: "image/png", sizes: "192x192", href: "/logo192.png" }],
  ]
});
