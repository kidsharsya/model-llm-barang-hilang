from fastapi import FastAPI
from sentence_transformers import SentenceTransformer, util
from pydantic import BaseModel
from typing import List
import numpy as np

app = FastAPI()
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

class MatchRequest(BaseModel):
    hilang: List[str]
    temuan: List[str]

@app.post("/cocokkan")
def cocokkan_laporan(req: MatchRequest):
    hilang_embeddings = model.encode(req.hilang, convert_to_tensor=True)
    temuan_embeddings = model.encode(req.temuan, convert_to_tensor=True)

    results = []
    for i, h in enumerate(hilang_embeddings):
        similarities = util.cos_sim(h, temuan_embeddings)[0].cpu().numpy()
        best_idx = int(np.argmax(similarities))
        best_score = float(similarities[best_idx])
        results.append({
            "index_hilang": i,
            "index_temuan": best_idx,
            "similarity": best_score
        })

    return results
