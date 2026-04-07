import { Component, OnInit, HostListener } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ResumeService } from '../../services/resume.service';

@Component({
  selector: 'app-download-button',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './download-button.component.html',
  styleUrls: ['./download-button.component.scss']
})
export class DownloadButtonComponent implements OnInit {
  isVisible = true;
  isFooterVisible = false;
  isAnimating = false;

  constructor(private resumeService: ResumeService) {}

  ngOnInit(): void {}

  @HostListener('window:scroll', [])
  onWindowScroll() {
    // Check if footer is visible
    const footer = document.querySelector('footer');
    if (footer) {
      const footerRect = footer.getBoundingClientRect();
      // Start hiding when footer is approaching viewport
      const footerApproaching = footerRect.top < window.innerHeight + 100;

      // Smooth transition based on footer position
      if (footerApproaching) {
        this.isFooterVisible = true;
        this.isVisible = false;
      } else {
        this.isFooterVisible = false;
        this.isVisible = true;
      }
    }
  }

  downloadResume() {
    this.isAnimating = true;
    setTimeout(() => {
      // Generate and download the resume PDF
      this.resumeService.generateResume();

      setTimeout(() => {
        this.isAnimating = false;
      }, 1000);
    }, 600);
  }
}
