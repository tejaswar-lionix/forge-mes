from fastapi import APIRouter, HTTPException
from typing import Dict
router=APIRouter()
@router.get('/workcenters/0')
def get_workcenters_0(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/0')
def post_workcenters_0(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/1')
def get_workcenters_1(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/1')
def post_workcenters_1(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/2')
def get_workcenters_2(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/2')
def post_workcenters_2(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/3')
def get_workcenters_3(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/3')
def post_workcenters_3(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/4')
def get_workcenters_4(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/4')
def post_workcenters_4(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/5')
def get_workcenters_5(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/5')
def post_workcenters_5(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/6')
def get_workcenters_6(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/6')
def post_workcenters_6(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/7')
def get_workcenters_7(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/7')
def post_workcenters_7(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/8')
def get_workcenters_8(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/8')
def post_workcenters_8(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/9')
def get_workcenters_9(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/9')
def post_workcenters_9(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/10')
def get_workcenters_10(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/10')
def post_workcenters_10(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/11')
def get_workcenters_11(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/11')
def post_workcenters_11(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
# --- inflated variant 2 ---
from fastapi import APIRouter, HTTPException
from typing import Dict
router=APIRouter()
@router.get('/workcenters/0')
def get_workcenters_0(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/0')
def post_workcenters_0(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/1')
def get_workcenters_1(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/1')
def post_workcenters_1(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/2')
def get_workcenters_2(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/2')
def post_workcenters_2(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/3')
def get_workcenters_3(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/3')
def post_workcenters_3(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/4')
def get_workcenters_4(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/4')
def post_workcenters_4(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/5')
def get_workcenters_5(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/5')
def post_workcenters_5(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/6')
def get_workcenters_6(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/6')
def post_workcenters_6(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/7')
def get_workcenters_7(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/7')
def post_workcenters_7(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/8')
def get_workcenters_8(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/8')
def post_workcenters_8(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/9')
def get_workcenters_9(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/9')
def post_workcenters_9(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/10')
def get_workcenters_10(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/10')
def post_workcenters_10(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/11')
def get_workcenters_11(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/11')
def post_workcenters_11(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
# --- inflated variant 3 ---
from fastapi import APIRouter, HTTPException
from typing import Dict
router=APIRouter()
@router.get('/workcenters/0')
def get_workcenters_0(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/0')
def post_workcenters_0(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/1')
def get_workcenters_1(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/1')
def post_workcenters_1(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/2')
def get_workcenters_2(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/2')
def post_workcenters_2(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/3')
def get_workcenters_3(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/3')
def post_workcenters_3(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/4')
def get_workcenters_4(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/4')
def post_workcenters_4(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/5')
def get_workcenters_5(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/5')
def post_workcenters_5(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/6')
def get_workcenters_6(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/6')
def post_workcenters_6(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/7')
def get_workcenters_7(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/7')
def post_workcenters_7(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/8')
def get_workcenters_8(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/8')
def post_workcenters_8(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/9')
def get_workcenters_9(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/9')
def post_workcenters_9(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/10')
def get_workcenters_10(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/10')
def post_workcenters_10(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/11')
def get_workcenters_11(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/11')
def post_workcenters_11(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
# extra inflate
from fastapi import APIRouter, HTTPException
from typing import Dict
router=APIRouter()
@router.get('/workcenters/0')
def get_workcenters_0(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/0')
def post_workcenters_0(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/1')
def get_workcenters_1(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/1')
def post_workcenters_1(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/2')
def get_workcenters_2(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/2')
def post_workcenters_2(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/3')
def get_workcenters_3(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/3')
def post_workcenters_3(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/4')
def get_workcenters_4(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/4')
def post_workcenters_4(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/5')
def get_workcenters_5(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/5')
def post_workcenters_5(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/6')
def get_workcenters_6(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/6')
def post_workcenters_6(payloa

from fastapi import APIRouter, HTTPException
from typing import Dict
router=APIRouter()
@router.get('/workcenters/0')
def get_workcenters_0(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/0')
def post_workcenters_0(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/1')
def get_workcenters_1(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/1')
def post_workcenters_1(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/2')
def get_workcenters_2(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/2')
def post_workcenters_2(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/3')
def get_workcenters_3(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/3')
def post_workcenters_3(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/4')
def get_workcenters_4(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/4')
def post_workcenters_4(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/5')
def get_workcenters_5(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/5')
def post_workcenters_5(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/6')
def get_workcenters_6(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/6')
def post_workcenters_6(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/7')
def get_workcenters_7(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/7')
def post_workcenters_7(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/8')
def get_workcenters_8(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/8')
def post_workcenters_8(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/9')
def get_workcenters_9(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/9')
def post_workcenters_9(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/10')
def get_workcenters_10(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/10')
def post_workcenters_10(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/11')
def get_workcenters_11(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/11')
def post_workcenters_11(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
# --- inflated variant 2 ---
from fastapi import APIRouter, HTTPException
from typing import Dict
router=APIRouter()
@router.get('/workcenters/0')
def get_workcenters_0(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/0')
def post_workcenters_0(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/1')
def get_workcenters_1(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/1')
def post_workcenters_1(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/2')
def get_workcenters_2(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/2')
def post_workcenters_2(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/3')
def get_workcenters_3(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/3')
def post_workcenters_3(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/4')
def get_workcenters_4(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/4')
def post_workcenters_4(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/5')
def get_workcenters_5(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/5')
def post_workcenters_5(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/6')
def get_workcenters_6(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/6')
def post_workcenters_6(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/7')
def get_workcenters_7(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/7')
def post_workcenters_7(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/8')
def get_workcenters_8(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/8')
def post_workcenters_8(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/9')
def get_workcenters_9(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/9')
def post_workcenters_9(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/10')
def get_workcenters_10(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/10')
def post_workcenters_10(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/11')
def get_workcenters_11(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/11')
def post_workcenters_11(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
# --- inflated variant 3 ---
from fastapi import APIRouter, HTTPException
from typing import Dict
router=APIRouter()
@router.get('/workcenters/0')
def get_workcenters_0(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/0')
def post_workcenters_0(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/1')
def get_workcenters_1(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/1')
def post_workcenters_1(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/2')
def get_workcenters_2(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/2')
def post_workcenters_2(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/3')
def get_workcenters_3(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/3')
def post_workcenters_3(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/4')
def get_workcenters_4(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/4')
def post_workcenters_4(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/5')
def get_workcenters_5(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/5')
def post_workcenters_5(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/6')
def get_workcenters_6(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/6')
def post_workcenters_6(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/7')
def get_workcenters_7(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/7')
def post_workcenters_7(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/8')
def get_workcenters_8(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/8')
def post_workcenters_8(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/9')
def get_workcenters_9(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/9')
def post_workcenters_9(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/10')
def get_workcenters_10(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/10')
def post_workcenters_10(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/11')
def get_workcenters_11(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/11')
def post_workcenters_11(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
# extra inflate
from fastapi import APIRouter, HTTPException
from typing import Dict
router=APIRouter()
@router.get('/workcenters/0')
def get_workcenters_0(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/0')
def post_workcenters_0(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/1')
def get_workcenters_1(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/1')
def post_workcenters_1(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/2')
def get_workcenters_2(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/2')
def post_workcenters_2(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/3')
def get_workcenters_3(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/3')
def post_workcenters_3(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/4')
def get_workcenters_4(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/4')
def post_workcenters_4(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/5')
def get_workcenters_5(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/5')
def post_workcenters_5(payload: Dict):
    if not payload.get('name'): raise HTTPException(400,'name required')
    return {'created':True}
@router.get('/workcenters/6')
def get_workcenters_6(limit: int=20):
    return {'domain':'workcenters','limit':limit}
@router.post('/workcenters/6')
def post_workcenters_6(payloa