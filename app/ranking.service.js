System.register([], function(exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var RankingService;
    return {
        setters:[],
        execute: function() {
            RankingService = (function () {
                function RankingService() {
                }
                RankingService.prototype.getPlayers = function () {
                    return [{ name: 'Sebastian', points: 9, games: 3 },
                        { name: 'Łukasz', points: 8, games: 2 },
                        { name: 'Wojciech', points: 7, games: 1 },
                        { name: 'Aleksandra', points: 6, games: 0 }];
                };
                return RankingService;
            }());
            exports_1("RankingService", RankingService);
        }
    }
});
//# sourceMappingURL=ranking.service.js.map