import {Component} from 'angular2/core';

@Component({
    selector: 'my-app',
    template: `
<h1>Hello {{name}}</h1>
<p>You clicked {{count}} times.</p>
<button (click)="countButton()">Count</button>
<button (click)="resetCountButton()">Reset</button>
`
})
export class AppComponent {
	name = 'x9663605';
	count = 0;

	countButton(){
		this.count += 1
	}
	resetCountButton(){
		this.count = 0
	}
}