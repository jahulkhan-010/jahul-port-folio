import { Routes } from '@angular/router';
import { HomePageComponent } from './components/home-page/home-page.component';
import { PrivacyPolicyComponent } from './components/privacy-policy/privacy-policy.component';
import { TermsOfUseComponent } from './components/terms-of-use/terms-of-use.component';

export const routes: Routes = [
  { path: '', component: HomePageComponent, pathMatch: 'full' },
  { path: 'about', component: HomePageComponent },
  { path: 'experience', component: HomePageComponent },
  { path: 'projects', component: HomePageComponent },
  { path: 'contact', component: HomePageComponent },
  { path: 'privacy', component: PrivacyPolicyComponent },
  { path: 'terms', component: TermsOfUseComponent },
  { path: '**', redirectTo: '' }
];
