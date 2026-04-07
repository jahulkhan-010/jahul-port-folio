import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ScrollService } from '../../services/scroll.service';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss'],
  imports: [RouterLink],
  standalone: true
})
export class FooterComponent implements OnInit {
  currentYear: number = new Date().getFullYear();

  constructor(private scrollService: ScrollService) {}

  ngOnInit(): void {
  }

  navigateToSection(fragment: string): void {
    this.scrollService.scrollToSection(fragment);
  }
}
