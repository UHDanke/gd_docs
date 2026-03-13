import { defineConfig } from 'vitepress'
import sidebar from './sidebar.mts';

export default defineConfig({
  srcDir: "docs",
  title: "HDanke's GD Docs",
  description: "HDanke's Editor Documentation",
  lang: 'en-US',
  cleanUrls: true,
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Triggers', link: '/triggers/general/trigger_activation' },
      { text: 'Editor', link: '/editor/autobuild' },
      { text: 'Bugs', link: '/bugs/README' },
      { text: 'Suggestions', link: '/suggestions/README' },
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
  }
});
