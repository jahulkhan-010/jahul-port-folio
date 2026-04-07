import { Component, OnInit, HostListener, Renderer2 } from '@angular/core';
import { ThemeService } from '../../services/theme.service';
import { RouterLink } from '@angular/router';
import { ScrollService } from '../../services/scroll.service';
import { ResumeService } from '../../services/resume.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent implements OnInit {
  isDarkTheme = true;
  isMobileMenuOpen = false;

  constructor(
    private themeService: ThemeService,
    private renderer: Renderer2,
    private scrollService: ScrollService,
    private resumeService: ResumeService
  ) {}

  ngOnInit(): void {
    this.themeService.isDarkTheme$.subscribe(isDark => {
      this.isDarkTheme = isDark;
    });
  }

  navigateToSection(fragment: string): void {
    this.scrollService.scrollToSection(fragment);
    this.closeMobileMenu();
  }

  toggleTheme(): void {
    this.themeService.toggleTheme();
  }

  toggleMobileMenu(): void {
    this.isMobileMenuOpen = !this.isMobileMenuOpen;
    if (this.isMobileMenuOpen) {
      this.renderer.addClass(document.body, 'no-scroll');
    } else {
      this.renderer.removeClass(document.body, 'no-scroll');
    }
  }

  closeMobileMenu(): void {
    if (this.isMobileMenuOpen) {
      this.isMobileMenuOpen = false;
      this.renderer.removeClass(document.body, 'no-scroll');
    }
  }

  @HostListener('window:resize', ['$event'])
  onResize(event: any): void {
    if (window.innerWidth > 992 && this.isMobileMenuOpen) {
      this.closeMobileMenu();
    }
  }

  downloadResume() {
    // Generate and download the resume PDF
    this.resumeService.generateResume();
  }
}
