import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ITrade } from 'src/app/models/trades';
import { TradesService } from 'src/app/services/trades.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  date="";
  trades!:ITrade[];

  constructor(private _tradeServices: TradesService,private router:Router) { }

  ngOnInit(): void {
  }
  searchClick(date:any){
    this._tradeServices.GetAllTrades(date).subscribe(
      response=>{
        this.trades=response;
      }
    )
  }

}
