import { Injectable } from '@angular/core';
import { Router, NavigationEnd, Scroll } from '@angular/router';
import { filter, delay } from 'rxjs/operators';
import { ViewportScroller } from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class ScrollService {
  constructor(
    private router: Router,
    private viewportScroller: ViewportScroller
  ) {
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd)
    ).subscribe(() => {
      this.scrollToFragment();
    });

    this.router.events.pipe(
      filter(e => e instanceof Scroll),
      delay(100)
    ).subscribe((e: Scroll) => {
      if (e.position) {
        this.viewportScroller.scrollToPosition(e.position);
      } else if (e.anchor) {
        this.viewportScroller.scrollToAnchor(e.anchor);
      } else {
        this.viewportScroller.scrollToPosition([0, 0]);
      }
    });
  }

  scrollToFragment(): void {
    const fragment = this.router.parseUrl(this.router.url).fragment;
    if (fragment) {
      setTimeout(() => {
        const element = document.getElementById(fragment);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }, 300);
    } else {
      window.scrollTo(0, 0);
    }
  }

  scrollToSection(fragment: string): void {
    let routePath = '/';

    if (fragment !== 'home') {
      routePath = `/${fragment}`;
    }

    this.router.navigate([routePath]).then(() => {
      setTimeout(() => {
        const element = document.getElementById(fragment);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }, 300);
    });
  }
}
