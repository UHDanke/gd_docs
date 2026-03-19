import { defineConfig } from 'vitepress'
import sidebar from './sidebar.mts';

export default defineConfig({
  base: '/gd_docs/',
  srcDir: "docs",
  markdown: {
    math: {
     chtml: {
       displayAlign: 'left'
     },
     svg: {
       displayAlign: 'left'
     }
    }
  },
  title: "HDanke's GD Editor Docs",
  description: "HDanke's Geometry Dash Editor Documentation",
  lang: 'en-US',
  cleanUrls: true,
  themeConfig: {
    socialLinks: [
      { icon: 'github', link: 'https://github.com/UHDanke/gd_docs' }
    ],
    sidebar: sidebar,
    lastUpdated: {
      text: 'Last updated',
      formatOptions: {
        dateStyle: 'medium',
        timeStyle: undefined
      }
    },
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