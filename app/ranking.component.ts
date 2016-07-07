import {Component} from 'angular2/core';
import {RankingService} from './ranking.service';

@Component({
    selector: 'ranking',
    template: `
	<ul>
	<li *ngFor="#player of players">{{ player.name }} ({{ player.points }})</li>
	</ul>
	`,
	providers: [RankingService]
})
export class RankingComponent {
	players;

	constructor(rankingService: RankingService){
		this.players = rankingService.getPlayers();
	}
}