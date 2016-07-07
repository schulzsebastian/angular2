import {Component} from 'angular2/core';
import {RankingComponent} from './ranking.component'

@Component({
    selector: 'my-app',
    template: `
	<h1>Ranking</h1>
	<ranking></ranking>
	`,
	directives: [RankingComponent]
})
export class AppComponent { }