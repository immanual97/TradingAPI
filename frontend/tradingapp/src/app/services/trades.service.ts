import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ITrade } from '../models/trades';

@Injectable({
  providedIn: 'root'
})
export class TradesService {

  constructor(private _http:HttpClient) { }

  GetAllTrades(date:string):Observable<ITrade[]>{
    let trad=this._http.get<ITrade[]>('http://127.0.0.1:8000/getallrecordbydate/'+date);
    return trad;
  }

}
